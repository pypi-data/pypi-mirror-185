/* eslint-disable react/prop-types */
import React from 'react';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const LessonList = ({ weeks, onLessonSelected }) => {
  let weekCnt = 1;
  //let chapterCnt = 1;

  return weeks
    .filter((week) => week.chapters)
    .map((week) => (
      <article className="flex w-full items-start space-x-6 py-12 px-4" key={weekCnt}>
        <p className="w-16 text-xl font-extrabold color-mint">{weekCnt++}주차</p>
        <div className="min-w-0 relative flex-auto pl-6">
          {week.chapters.map((chapter) => (
            <div
              key={chapter.lessonId}
              className="w-full bg-white border-t-2 sm:p-6 dark:bg-gray-800 dark:border-gray-700 color-mint"
            >
              <h5 className="mb-3 text-base font-semibold text-teal-500 lg:text-xl dark:text-white">
                {chapter.title}
              </h5>
              <ul className="my-5 space-y-3">
                {chapter.lessons &&
                  chapter.lessons.map((lesson) => (
                    <li key={lesson.lessonId}>
                      <a
                        href="#"
                        className="flex items-center p-3 text-base font-bold rounded-lg group border border-gray-200 bg-white hover:bg-gray-100 text-gray-900"
                        onClick={() => onLessonSelected(lesson.lessonId)}
                      >
                        <span className="flex-1 ml-3 whitespace-nowrap">
                          {lesson.title}
                        </span>
                        {/* <span className="inline-flex items-center justify-center px-2 py-0.5 ml-3 text-xs font-medium text-gray-500 bg-gray-200 rounded dark:bg-gray-700 dark:text-gray-400">
                  Popular
                </span> */}
                      </a>
                    </li>
                  ))}
              </ul>
            </div>
          ))}
        </div>
      </article>
    ));
};

export default LessonList;
