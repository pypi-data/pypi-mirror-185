/* eslint-disable react/prop-types */
import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { config } from '../config/config';
import LectureCard from './useLectureCard';
import LectureDetail from './useLectureDetail';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const LectureList = ({
  getToken,
  onLectureSelected,
  onLessonSelected,
  onLessonLoaded,
  onResetCategory,
}) => {
  const [pageNo, setPageNo] = useState(1);
  const [lectures, setLectures] = useState([]);
  const [lecture, setLecture] = useState(null);

  const wait = (timeToDelay) =>
    new Promise((resolve) => setTimeout(resolve, timeToDelay));

  // 컴포넌트가 로드될 때 실행 되고, 두번째 인자로 주어진 배열에 포함된 특정값이 업데이트될때마다 실행됨
  // 한 번만 실행되게 하려면 빈 배열을 사용
  useEffect(() => {
    async function loadLectureList() {
      try {
        const response = await axios.get(
          `${config.baseUrl}Lecture/Applied?pageNo=${pageNo}&useJupyter=1`,
          {
            headers: {
              Authorization: `Bearer ${getToken()}`,
            },
          }
        );

        setLectures([]);
        setLectures((prev) => [...prev, ...response.data.data]);
      } catch (err) {
        if (axios.isAxiosError(err) && err.response) {
          console.log(err);
        } else {
          console.log(err);
        }
      }
    }

    loadLectureList();
  }, [pageNo]);

  const onResetLessonSelected = () => {
    setLecture(null);
  };

  return (
    <div className="container mx-auto">
      {/* <div className="wrapper">
        {lectures.map((lecture, index) => (
          <LectureAccordion
            key={lecture.lectureId}
            lecture={lecture}
            getToken={getToken}
            onLessonSelected={onLessonSelected}
          ></LectureAccordion>
        ))}
      </div> */}

      {!lecture && (
        <>
          <button
            className="ml-8 mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50"
            onClick={onResetCategory}
          >
            <i className='mdi mdi-chevron-left text-sm'></i>
            유형 선택으로
          </button>
          <div className="grid gap-8 grid-cols-3 ml-8 mr-8">
            {lectures.map((lecture, index) => (
              <LectureCard
                key={lecture.lectureId}
                onLectureSelected={() => {
                  setLecture(lecture);
                  onLectureSelected(lecture);
                }}
                lecture={lecture}
              />
            ))}
          </div>
        </>
      )}
      {lecture && (
        <LectureDetail
          lecture={lecture}
          getToken={getToken}
          onLessonSelected={onLessonSelected}
          onResetLessonSelected={onResetLessonSelected}
          onLessonLoaded={onLessonLoaded}
        />
      )}
    </div>
  );
};

export default LectureList;
