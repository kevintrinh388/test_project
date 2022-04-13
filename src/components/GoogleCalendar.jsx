/* eslint-disable react/jsx-props-no-spreading */
import React, { useState } from 'react';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import { toast } from 'react-toastify';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers';
import TextField from '@mui/material/TextField';

function GoogleCalendar() {
  const [dateTime, setDateTime] = useState(null);
  const [endDateTime, setEndDateTime] = useState(null);

  function dateTimeHandler(e) {
    setDateTime(e.toISOString());
    console.log(dateTime);
    e.setHours(e.getHours() + 1);
    setEndDateTime(e.toISOString());
    console.log(endDateTime);
  }

  function buttonHandler() {
    if (dateTime === undefined) {
      toast.error('No date entered', {
        toastId: 'error1',
        position: 'bottom-center',
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    } else {
      toast.success(`${dateTime} added to calendar`, {
        toastId: 'success1',
        position: 'bottom-center',
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    }
  }

  return (
    <div>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DateTimePicker
          renderInput={(props) => <TextField {...props} />}
          label="Enter date"
          value={dateTime}
          inputformat="yyyy-MM-dd HH:mm:ss"
          onChange={(e) => dateTimeHandler(e)}
        />
        <button type="button" onClick={() => buttonHandler()}>Add to google calendar</button>
      </LocalizationProvider>
    </div>
  );
}

export default GoogleCalendar;