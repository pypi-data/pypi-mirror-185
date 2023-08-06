/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable react/no-unescaped-entities */
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { config } from '../config/config';
import LessonList from './useLessonList';

const LectureDetail = ({
  lecture,
  getToken,
  onLessonSelected,
  onResetLessonSelected,
  onLessonLoaded,
}: any) => {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    (async () => {
      const response = await axios.get(
        `${config.baseUrl}Lecture/${lecture.lectureId}/Lessons`,
        {
          headers: {
            Authorization: `Bearer ${getToken()}`,
          },
        }
      );

      // 주차 - 회차 - 강의 구조 구성
      const _lessons = [];
      let currentWeek = null;
      let currentChapter = null;
      for (const lesson of response.data.data) {
        if (lesson.type === 'week') {
          _lessons.push(lesson);
          currentWeek = lesson;
        } else if (lesson.type === 'chapter') {
          if (!currentWeek.chapters) {
            currentWeek.chapters = [];
          }
          currentWeek.chapters.push(lesson);
          currentChapter = lesson;
        } else {
          if (!currentChapter.lessons) {
            currentChapter.lessons = [];
          }
          currentChapter.lessons.push(lesson);
        }
      }
      setLessons([]);
      // 기존 데이터를 무시하고 새 데이터만 넣는다.
      setLessons((prev) => [..._lessons]);
      onLessonLoaded(_lessons);
    })();
  }, [lecture]);

  const getSanitizedData = (data) => ({
    __html: data,
  });

  return (
    <section className="text-gray-700 body-font overflow-hidden bg-white">
      <div className="container-xl px-5 mx-auto">
        <div className="mx-auto flex flex-wrap">
          <div className="w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0">
            <button
              className="mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50"
              onClick={onResetLessonSelected}
            >
              <i className='mdi mdi-chevron-left text-sm'></i>
              강좌 목록으로
            </button>
            <h1 className="text-gray-900 text-xl title-font font-extrabold mb-5">
              {lecture.title}
            </h1>
            <p
              className="leading-relaxed text-xs"
              dangerouslySetInnerHTML={getSanitizedData(lecture.description)}
            ></p>
            <div className="flex items-center pb-5 border-b border-gray-200">
              <div className="flex ml-6 items-center">
                <div className="relative">
                  <span className="absolute right-0 top-0 h-full w-10 text-center text-gray-600 pointer-events-none flex items-center justify-center"></span>
                </div>
              </div>
            </div>
            {/* <div className="flex">
              <span className="title-font font-medium text-2xl text-gray-900"></span>
              <button className="flex ml-auto text-white bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-600 rounded">
                수강
              </button>
            </div> */}
            <div className="flex">
              {lessons.length > 0 && (
                <LessonList
                  weeks={lessons}
                  onLessonSelected={onLessonSelected}
                />
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default LectureDetail;
