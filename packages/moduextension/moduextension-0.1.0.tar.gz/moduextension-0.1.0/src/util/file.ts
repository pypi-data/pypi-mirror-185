/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
export const handleDownload = (fileUrl) => {
  try {
    if (!fileUrl.includes('___')) {
      return;
    }

    const filename = fileUrl.split('___')[1];
    const link = document.createElement('a');
    link.href = fileUrl;
    link.target = '_blank';
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (err) {
    console.log(err);
  }
};
