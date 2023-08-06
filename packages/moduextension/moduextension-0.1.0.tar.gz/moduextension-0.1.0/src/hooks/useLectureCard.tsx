import React from 'react';
import { getDateStringOnly } from '../util/date';

const LectureCard = ({ onLectureSelected, lecture }: any) => {
  return (
    <div
      className="
        card border border-gray-200 bg-white cursor-pointer p-5 rounded-md text-center
        max-h-80 max-w-80"
      onClick={onLectureSelected}
    >
      <img
        src={lecture.thumbnailUrl}
        alt={lecture.title}
        className="w-64 bg-gray-400 rounded-sm m-auto"
      />
      <span className="mt-3 font-large font-bold block">{lecture.title}</span>
      <span className="mt-2 text-gray-400">
        {lecture.last_lesson_date &&
          `마지막 수강일: ${getDateStringOnly(lecture.last_lesson_date)}`}
        {!lecture.last_lesson_date && '수강기록 없음'}
      </span>
    </div>
  );
};

export default LectureCard;
