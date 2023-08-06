/* eslint-disable react/prop-types */
import axios from 'axios';
import React, { useState } from 'react';
import { config } from '../config/config';
import '../../style/lecture-detail.css';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const QuestionAccordion = ({
  getToken,
  questionsData,
  onQuestionSelected,
  /*children,*/
}) => {
  const [isOpen, setOpen] = useState(false);
  const [questions, setQuestions] = useState([...questionsData]);

  return (
    <div className="accordion-wrapper">
      <div
        className={`accordion-title ${isOpen ? 'open' : ''}`}
        onClick={async () => {
          const isOpenState = !isOpen;
          setOpen(isOpenState);
        }}
      >
        문제 목록
      </div>
      <div className={`accordion-item2 ${!isOpen ? 'collapsed' : ''}`}>
        {/* <div className="accordion-content">{children}</div> */}
        <div className="accordion-content">
          <ul>
            {
              questions.map((question, index) => (
                <li key={question.questionId}>
                  <div>
                    {question.title}
                    <button
                      type="button"
                      onClick={async () => {
                        try {
                          const fileUrl =
                            'https://modustorage0.blob.core.windows.net/notebooks/31097142-C090-490E-8289-6F7B46723BFA___Sample.ipynb';
                          const filename = fileUrl.split('___')[1];
                          const response = await axios({
                            url: `${config.baseUrl}Files`,
                            method: 'POST',
                            responseType: 'blob',
                            data: {
                              fileUrl: encodeURIComponent(
                                'https://modustorage0.blob.core.windows.net/notebooks/31097142-C090-490E-8289-6F7B46723BFA___Sample.ipynb'
                              ),
                            },
                            headers: {
                              Authorization: `Bearer ${getToken()}`,
                            },
                          });

                          const url = window.URL.createObjectURL(
                            new Blob([response.data])
                          );
                          const link = document.createElement('a');
                          link.href = url;
                          link.setAttribute('download', filename);
                          document.body.appendChild(link);
                          link.click();
                          document.body.removeChild(link);
                        } catch (err) {
                          console.log(err);
                        }
                      }}
                    >
                      문제풀기
                    </button>
                  </div>
                </li>
              ))
              // lessons.map((lesson, index) => (
              //   <LessonAccordion
              //     title={lesson.title}
              //     lessonId={lesson.lessonId}
              //     getToken={getToken}
              //     onLessonSelected={onLessonSelected}
              //   ></LessonAccordion>
              // ))
            }
          </ul>
        </div>
      </div>
    </div>
  );
};

export default QuestionAccordion;
