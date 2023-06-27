// import { useState } from 'react';

function UploadButton({ label, fileType, id, pState }) {
    const {files, setFiles} = pState;
  
    // On file select (from the pop up)
    function onFileChange(event) {
      let fileInfos = files;
      var my_id = id;
  
      fileInfos[my_id] = event.target.files[0];
      setFiles(fileInfos);
    };
  
    return (
      <div>
        <label>{label}:&nbsp;&nbsp;
        <input type="file" accept={fileType} onChange={onFileChange} />
        </label>
      
      </div>
    );
  }
  
  export default UploadButton;
  
  /* <button onClick={onFileUpload}> Upload </button> */