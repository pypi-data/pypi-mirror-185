/* eslint-disable no-irregular-whitespace */
/* eslint-disable no-useless-escape */
/* eslint-disable @typescript-eslint/explicit-module-boundary-types */
/* eslint-disable jsdoc/require-returns */

/**
 * 유효한 url인지 확인
 * @param {String} url 확인할 url 문자열
 */
export const isValidUrl = (url: string) => {
  const regex =
    /(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g;

  return regex.test(url);
};

/**
 * 유효한 youtube url인지 확인
 * @param {String} url 확인할 youtube url 문자열
 */
export const isYoutubeUrl = (url: string) => {
  if (!url) {
    return false;
  }

  const youtubeUrlPattern =
    /http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?/gm;
  const found = url.match(youtubeUrlPattern);

  return found;
};
