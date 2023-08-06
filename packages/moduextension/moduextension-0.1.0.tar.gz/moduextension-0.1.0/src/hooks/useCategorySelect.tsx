import React from 'react';
import Category from '../types/category';
import GrayCenterContainer from './useGrayCenterContainer';

/**
 * https://flowbite.com/docs/components/card/#
 */

const CategorySelect = ({ onCategorySelected }: any) => {
  return (
    <GrayCenterContainer>
      <div className="category-popup p-4 max-w-sm rounded-lg border shadow-md sm:p-6 bg-white border-gray-200">
        <h5 className="mb-3 text-base font-semibold lg:text-xl text-gray-700">
          유형 선택하기
        </h5>
        <p className="text-sm font-normal text-gray-400">
          강좌를 선택하여 AI 학습을 진행하거나, AI 해커톤을 선택하여 경쟁에
          참여하세요.
        </p>
        <ul className="my-4 space-y-3">
          <li>
            <a
              href="#"
              className="flex items-center p-3 text-base font-bold rounded-lg group hover:bg-gray-100 border border-200"
              onClick={() => {
                onCategorySelected(Category.Lecture);
              }}
            >
              <span className="flex-1 ml-3 whitespace-nowrap">
                AI 강좌 학습하기
              </span>
              {/* <span className="inline-flex items-center justify-center px-2 py-0.5 ml-3 text-xs font-medium text-gray-500 bg-gray-200 rounded dark:bg-gray-700 dark:text-gray-400">
              Popular
            </span> */}
            </a>
          </li>
          <li>
            <a
              href="#"
              className="flex items-center p-3 text-base font-bold rounded-lg group hover:bg-gray-100 border border-200"
              onClick={() => {
                onCategorySelected(Category.AIHackathon);
              }}
            >
              <span className="flex-1 ml-3 whitespace-nowrap">
                AI 해커톤에 참가하기
              </span>
            </a>
          </li>
        </ul>
      </div>
    </GrayCenterContainer>
  );
};

export default CategorySelect;
