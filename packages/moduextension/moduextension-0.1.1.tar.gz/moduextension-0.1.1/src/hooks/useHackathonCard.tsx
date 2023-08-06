/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
import React from 'react';
import { getTimeBoxString } from '../util/date';

const HackathonCard = ({ hackathon, onHackathonSelected }: any) => {
  return (
    <a
      href="#"
      className="hackathon-card flex flex-col items-center border-b-2 md:flex-row md:max-w-full border-gray-200 py-7 px-12"
      onClick={onHackathonSelected}
    >
      <img
        className="object-cover w-full h-96 md:h-auto md:w-36 md:rounded-md"
        src={hackathon.thumbnailUrl}
        alt={hackathon.title}
      />
      <div className="flex flex-col justify-between py-4 leading-normal px-7">
        <div className="flex flex-start items-baseline">
          <h5 className="mb-6 text-lg font-bold tracking-tight">
            {hackathon.title}
          </h5>
          {hackathon.isSubmitted && (
            <span className="inline-flex items-center justify-center h-6 px-2 py-0.5 ml-3 text-xs font-medium rounded bg-gray-400 text-gray-100">
              제출완료
            </span>
          )}
        </div>

        <p className="mb-3 font-normal text-gray-400">
          진행 기간 :{' '}
          {getTimeBoxString(`${hackathon.startDate}Z`, `${hackathon.endDate}Z`)}
        </p>
      </div>
    </a>
  );
};

export default HackathonCard;
