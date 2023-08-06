import React, { useMemo } from 'react';
import { AzureMP } from 'react-azure-mp';

const AzureMediaPlayer = (videoUrl) => {
  const src = useMemo(
    () => [{ src: videoUrl, type: 'application/vnd.ms-sstr+xml' }],
    []
  );
  return <AzureMP skin="amp-flush" src={src} />;
};

export default AzureMediaPlayer;
