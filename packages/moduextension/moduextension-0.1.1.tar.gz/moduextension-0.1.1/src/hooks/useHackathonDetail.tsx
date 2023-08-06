/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { config } from '../config/config';
import { getTimeBoxString } from '../util/date';
import { handleDownload } from '../util/file';

const HackathonDetail = ({
  getToken,
  hackathonId,
  onResetHackathonSelected,
}: any) => {
  const [hackathon, setHackathon] = useState(null);
  const [files, setFiles] = useState(null);
  const [onProcess, setOnProcess] = useState(false);

  useEffect(() => {
    (async () => {
      try {
        const response = await axios.get(
          `${config.baseUrl}Test/${hackathonId}`,
          {
            headers: {
              Authorization: `Bearer ${getToken()}`,
            },
          }
        );

        const fileUrlResponse = await axios.get(
          `${config.baseUrl}Test/${hackathonId}/SubmittedFileUrl`,
          {
            headers: {
              Authorization: `Bearer ${getToken()}`,
            },
          }
        );

        const hackathonData = response.data.data;

        if (fileUrlResponse.data && fileUrlResponse.data.result) {
          hackathonData.submittedFileUrl =
            fileUrlResponse.data.submittedFileUrl;
        }

        // 기존 데이터 무시하고 새로 채우기
        setHackathon(hackathonData);
      } catch (err: any) {
        console.error(err);
      }
    })();
  }, []);

  const getSanitizedData = (data) => ({
    __html: data,
  });

  const isFileSelected = React.useCallback(() => {
    return files && files.length > 0;
  }, [files]);

  const uploadNotebookFile = React.useCallback(() => {
    (async () => {
      try {
        setOnProcess(true);
        const formData = new FormData();
        formData.append('testId', hackathon.testId);
        formData.append('notebookFiles', files.item(0));

        const response = await axios.post(
          `${config.baseUrl}Test/Submit`,
          formData,
          {
            headers: {
              Authorization: `Bearer ${getToken()}`,
              'Content-Type': 'multipart/form-data',
            },
          }
        );

        if (response.data && response.data.result) {
          alert('파일 업로드가 완료 되었습니다.');

          setHackathon((prev) => ({
            ...prev,
            ['submittedFileUrl']: response.data.notebookFileUrl,
          }));
        } else {
          alert('파일 업로드 중 오류가 발생했습니다.');
        }
      } catch (err: any) {
        console.error(err);
        alert('파일 업로드 중 오류가 발생했습니다.');
      } finally {
        setOnProcess(false);
      }
    })();
  }, [files]);

  return (
    <>
      <button
        className="mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50"
        onClick={onResetHackathonSelected}
      >
        <i className='mdi mdi-menu text-sm mr-1'></i>
        목록으로
      </button>
      {hackathon && (
        <div className="relative py-7 pl-8 border-b-2 border-t-2 border-gray-200 sm:mx-auto sm:max-w-3/6 sm:px-10">
          <div className="w-full">
            <div className="flex flex-row flex-start">
              <img
                src={hackathon.thumbnailUrl}
                className="h-50 w-60 rounded-md"
                alt={hackathon.title}
              />
              <div className="flex-col ml-6">
                <div className="mt-10 text-4xl leading-7">
                  <div className="flex flex-start items-center">
                    <h1 className='font-bold text-xl'>{hackathon.title}</h1>
                    {hackathon.submittedFileUrl && (
                      <span className="bg-gray-400 h-6 inline-flex items-center ml-3 px-2 py-0.5 rounded text-gray-100 text-xs">
                        제출완료
                      </span>
                    )}
                  </div>
                </div>

                <span className="font-semibold inline-block mt-6 text-gray-400">
                  진행 기간 :{' '}
                  {getTimeBoxString(
                    `${hackathon.startDate}Z`,
                    `${hackathon.endDate}Z`
                  )}
                </span>
              </div>
            </div>

            <div className='divide-y divide-gray-100'>
              <div className="py-8 text-base leading-7">
                <p className='font-bold'
                  dangerouslySetInnerHTML={getSanitizedData(hackathon.content)}
                ></p>

                <p className='pt-5'>
                  <a
                    href="#"
                    className="border rounded py-1 px-4 hover:bg-gray-100 text-gray-600 text-sm"
                    onClick={() => {
                      handleDownload(hackathon.uploadFileUrl);
                    }}
                  >
                    <i className='mdi mdi-arrow-down-bold-outline text-sm mr-1'></i>
                    노트북 파일 다운로드
                  </a>
                </p>
              </div>
              <div className="pt-8 text-base leading-7">
                <p className="text-xl font-bold">
                  결과 파일 업로드하기
                </p>
                {hackathon.submittedFileUrl && (
                  <p className='pt-5'>
                    <a
                      href="#"
                      className="border rounded py-1 px-4 hover:bg-gray-100 text-gray-600 text-sm"
                      onClick={() => {
                        handleDownload(hackathon.submittedFileUrl);
                      }}
                    >
                      <i className='mdi mdi-arrow-down-bold-outline text-sm mr-1'></i>
                      제출한 파일 다운로드
                    </a>
                  </p>
                )}
                <div className="flex flex-row flex-start mt-6">
                  <input
                    className="block border-b w-2/6 text-sm cursor-pointer text-gray-400 focus:outline-none placeholder-gray-400"
                    aria-describedby="file_input_help"
                    id="file_input"
                    type="file"
                    accept=".ipynb"
                    onChange={(e) => setFiles(e.target.files)}
                  />
                  {isFileSelected() && (
                    <button
                      className="bg-gray-400 hover:bg-gray-500 text-white text-sm rounded px-1 disabled:bg-slate-50 ml-3 w-24"
                      onClick={uploadNotebookFile}
                      disabled={onProcess}
                    >
                      {onProcess ? (
                        <svg
                          role="status"
                          className="inline w-4 h-4 mr-3 text-white animate-spin"
                          viewBox="0 0 100 101"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="#E5E7EB"
                          />
                          <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentColor"
                          />
                        </svg>
                      ) : (
                        '업로드 하기'
                      )}
                    </button>
                  )}
                </div>
                <p className="mt-1.5 text-sm text-blue-400" id="file_input_help">
                  ipynb 파일 형식만 가능합니다.
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default HackathonDetail;
