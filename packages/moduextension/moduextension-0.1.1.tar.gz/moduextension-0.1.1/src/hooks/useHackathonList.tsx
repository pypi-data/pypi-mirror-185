/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import HackathonCard from './useHackathonCard';
import { config } from '../config/config';
import HackathonDetail from './useHackathonDetail';

const HackathonList = ({ getToken, onResetCategory }: any) => {
  const [pageNo, setPageNo] = useState(1);
  const [hackathons, setHackathons] = useState([]);
  const [hackathonId, setHackathonId] = useState(0);

  useEffect(() => {
    (async () => {
      await loadList();
    })();
  }, [pageNo]);

  const loadList = async () => {
    try {
      const response = await axios.get(`${config.baseUrl}Test?type=5`, {
        headers: {
          Authorization: `Bearer ${getToken()}`,
        },
      });

      // 기존 데이터 무시하고 새로 채우기
      setHackathons([...response.data.result]);
    } catch (err) {
      if (axios.isAxiosError(err) && err.response) {
        console.log(err);
      } else {
        console.log(err);
      }
    }
  };

  const onResetHackathonSelected = () => {
    setHackathonId(0);
  };

  const onRefreshList = async () => {
    await loadList();
  };

  return (
    <div className="container mx-auto overflow-auto h-5/6">
      {!hackathonId ? (
        <>
          <button
            className="mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 ml-8 py-1 disabled:bg-slate-50"
            onClick={onResetCategory}
          >
            <i className="mdi mdi-chevron-left text-sm mr-1"></i>
            유형 선택으로
          </button>
          <button
            className="mb-7 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 ml-5 py-1 disabled:bg-slate-50"
            onClick={onRefreshList}
          >
            <i className="mdi mdi-refresh text-sm mr-1"></i>
            새로 고침
          </button>
          <div className="grid grid-cols-1 ml-8 mr-8">
            {hackathons.map((hackathon) => (
              <HackathonCard
                key={hackathon.testId}
                hackathon={hackathon}
                onHackathonSelected={() => {
                  setHackathonId(hackathon.testId);
                }}
              />
            ))}
          </div>
        </>
      ) : (
        <HackathonDetail
          getToken={getToken}
          hackathonId={hackathonId}
          onResetHackathonSelected={onResetHackathonSelected}
        />
      )}
    </div>
  );
};

export default HackathonList;
