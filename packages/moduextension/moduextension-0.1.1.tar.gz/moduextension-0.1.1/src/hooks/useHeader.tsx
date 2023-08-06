import React from "react";

const Header = ({
  lectureDrawerVisible,
  setIsOpen,
  getUser,
  lecture,
  lessons,
  handleBackToLectureList,
}: any) => {
  const { email, name } = getUser();
  return (
    <header className="flex justify-between p-4">
      {lectureDrawerVisible ? (
        <div>
          <button
            className="mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50"
            onClick={(e) => {
              e.stopPropagation();
              setIsOpen(true);
            }}
            disabled={!lectureDrawerVisible}
          >
            <i className="mdi mdi-menu text-sm mr-1"></i>
            강의 목록
          </button>
          <button
            className="ml-8 mb-5 border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-2 py-1 disabled:bg-slate-50"
            onClick={handleBackToLectureList}
            disabled={!lectureDrawerVisible}
          >
            <i className="mdi mdi-check text-sm mr-1"></i>
            강좌 선택
          </button>
        </div>
      ) : (
        <div></div>
      )}
      {lecture && <p className="text-bold">{lecture.title}</p>}
      <h1 className="font-medium">
        {name}({email})
      </h1>
    </header>
  );
};

export default Header;
