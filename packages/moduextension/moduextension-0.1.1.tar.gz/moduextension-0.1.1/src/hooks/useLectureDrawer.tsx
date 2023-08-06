import React from 'react';

const LectureDrawer = ({ children, isOpen, setIsOpen }: any) => {
  return (
    <main
      className={
        ' absolute overflow-hidden z-10 bg-gray-900 bg-opacity-25 inset-0 transform ease-in-out ' +
        (isOpen
          ? ' transition-opacity opacity-100 duration-500 translate-x-0  '
          : ' transition-all delay-500 opacity-0 translate-x-full  ')
      }
    >
      <section
        className={
          ' w-screen max-w-lg left-0 absolute bg-white h-full shadow-xl delay-400 duration-500 ease-in-out transition-all transform  ' +
          (isOpen ? ' translate-x-0 ' : ' -translate-x-full ')
        }
      >
        <article className="relative w-screen max-w-lg pb-10 flex flex-col space-y-6 overflow-y-scroll h-full">
          <div className="flex justify-between p-4">
            <header className="font-bold text-lg">강좌 목록</header>
            <button
              className="border border-gray-200 hover:bg-gray-100 text-gray-600 rounded px-4 py-1"
              onClick={() => setIsOpen(false)}
            >
              닫기
            </button>
          </div>
          {children}
        </article>
      </section>
      <section
        className=" w-screen h-full cursor-pointer "
        onClick={() => {
          setIsOpen(false);
        }}
      ></section>
    </main>
  );
};

export default LectureDrawer;
