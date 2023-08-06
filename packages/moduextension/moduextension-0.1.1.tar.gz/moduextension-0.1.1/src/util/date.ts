export const getTimeStringOnly = (dateString: string | null = null): string => {
  const date = dateString ? new Date(dateString) : new Date();

  return [
    ('0' + date.getHours()).slice(-2),
    ('0' + date.getMinutes()).slice(-2),
  ].join(':');
};

export const getDateStringOnly = (dateString: string): string => {
  if (!dateString) {
    return null;
  }
  const date = new Date(dateString);
  return [
    date.getFullYear(),
    ('0' + (date.getMonth() + 1)).slice(-2),
    ('0' + date.getDate()).slice(-2),
  ].join('-');
};

export const getTimeBoxString = (
  startDateString: string,
  endDateString: string
): string => {
  if (!startDateString || !endDateString) {
    return null;
  }

  return `${getDateStringOnly(startDateString)} ${getTimeStringOnly(
    startDateString
  )} ~ ${getDateStringOnly(endDateString)} ${getTimeStringOnly(endDateString)}`;
};
