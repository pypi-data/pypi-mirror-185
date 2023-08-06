import React from 'react';

const GrayCenterContainer = ({ children }: any) => {
  return (
    <section className="flex justify-center w-full gradient-form bg-gray-200 md:h-screen mx-auto">
      <div className="container max-w-6xl py-12 px-6 container-h-full">
        <div className="flex justify-center items-center flex-wrap container-h-full g-6 text-gray-800">
          {children}
        </div>
      </div>
    </section>
  );
};

export default GrayCenterContainer;
