import { useEffect } from 'react';

const useStyle = (url: string) => {
  useEffect(() => {
    const style = document.createElement('link');

    style.rel = 'stylesheet';
    style.href = url;

    document.head.appendChild(style);

    return () => {
      document.head.removeChild(style);
    };
  }, [url]);
};

export default useStyle;
