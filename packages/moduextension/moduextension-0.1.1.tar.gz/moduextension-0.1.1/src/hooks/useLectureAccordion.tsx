/* eslint-disable react/prop-types */
import axios from 'axios';
import React, { useState } from 'react';
import { config } from '../config/config';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const LectureAccordion = ({
  lecture,
  getToken,
  onLessonSelected,
  /*children,*/
}) => {
  const [isOpen, setOpen] = useState(false);
  const [lessons, setLessons] = useState([]);

  const wait = (timeToDelay) =>
    new Promise((resolve) => setTimeout(resolve, timeToDelay));

  let weekCnt = 1;
  let chapterCnt = 1;

  const renderLessonDetailList = (lessons) => {
    return lessons.map((lesson) => (
      <li key={lesson.lessonid}>
        <span className="depth"></span>
        <p id="listLessonTitle">{lesson.title}</p>
        <div className="right_part" style={{ display: 'block' }}>
          <button
            onClick={() => {
              onLessonSelected(lecture, lesson.lessonId);
            }}
          >
            학습하기
          </button>
        </div>
      </li>
    ));
  };

  const renderChapterList = (chapters) => {
    return chapters
      .filter((chapter) => chapter.lessons)
      .map((chapter) => (
        <li key={`chapter${chapterCnt}`} id={`chapter${chapterCnt}`}>
          <a href="javascript:;" className="acc_btn">
            <span className="nth">
              <u id="listChapterCnt">{chapterCnt++}</u>회차
            </span>
            <p className="nth_tit" id="listChapterTitle">
              {chapter.title}
            </p>
            <span className="arrow">
              <i className="icon chevron up"></i>
            </span>
          </a>
          <div style={{ display: 'block' }}>
            <ul id="appendLesson">{renderLessonDetailList(chapter.lessons)}</ul>
          </div>
        </li>
      ));
  };

  const renderWeekList = (weeks) => {
    return weeks
      .filter((week) => week.chapters)
      .map((week) => (
        <div
          className="weekly_plan_box"
          key={`week${weekCnt}`}
          id={`week${weekCnt}`}
        >
          <div className="left_week">
            <p className="circle">
              <span className="num" id="listWeekCnt">
                {weekCnt++}
              </span>
              주차
            </p>
            <span className="dash_line"></span>
          </div>
          <div className="right_plan">
            <p className="plan_tit" id="listWeekTitle"></p>
            <div className="plan_accordion">
              <ul id="appendChapter">{renderChapterList(week.chapters)}</ul>
            </div>
          </div>
        </div>
      ));
  };

  const renderLessonList = (lessons) => {
    const result = [];
    // let week = null;
    // let weekCnt = 1;
    // let chapter = null;
    // let chapterCnt = 1;

    // // 디스플레이하기 위한 카운트
    // let totalWeek = 0;
    // let totalLesson = 0;
    // let totalExam = 0;
    // let totalAssignment = 0;

    const _lessons = [];
    let currentWeek = null;
    let currentChapter = null;
    for (const lesson of lessons) {
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

    return (
      <div className="weekly_plan" id="appendLessons">
        {renderWeekList(_lessons)}
      </div>
    );
  };

  return (
    <div className="accordion-wrapper">
      <div
        className={`accordion-title ${isOpen ? 'open' : ''}`}
        onClick={async () => {
          const isOpenState = !isOpen;
          setOpen(isOpenState);

          if (isOpenState && lessons.length === 0) {
            try {
              const response = await axios.get(
                `${config.baseUrl}Lecture/${lecture.lectureId}/Lessons`,
                {
                  headers: {
                    Authorization: `Bearer ${getToken()}`,
                  },
                }
              );

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
              setLessons((prev) => [...prev, ..._lessons]);
            } catch (err) {
              if (axios.isAxiosError(err) && err.response) {
                console.log(err);
              } else {
                console.log(err);
              }
            }
          }
        }}
      >
        {lecture.title}
        {lecture.onAir ? ' (강의중)' : ''}
        <button
          type="button"
          className="btn btn-primary"
          onClick={(e) => {
            e.stopPropagation();
          }}
        >
          이어하기
        </button>
      </div>
      <div className={`accordion-item2 ${!isOpen ? 'collapsed' : ''}`}>
        {/* <div className="accordion-content">{children}</div> */}
        <div className="accordion-content">
          {/* <ul> */}
          <div className="weekly_plan" id="appendLessons">
            {lessons.length > 0 && renderWeekList(lessons)}
          </div>
          {
            // lessons.map((lesson, index) => (
            //   <LessonAccordion
            //     title={lesson.title}
            //     lessonId={lesson.lessonId}
            //     getToken={getToken}
            //     onLessonSelected={onLessonSelected}
            //   ></LessonAccordion>
            // ))
          }
          {/* </ul> */}
        </div>
      </div>
    </div>
  );
};

export default LectureAccordion;
