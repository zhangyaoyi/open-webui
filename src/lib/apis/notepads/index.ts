import { WEBUI_API_BASE_URL } from '$lib/constants';

export const getNotepad = async (token: string = '', chat_id: string) => {
  let error = null;

  const res = await fetch(`${WEBUI_API_BASE_URL}/notepads/${chat_id}`, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      ...(token && { authorization: `Bearer ${token}` })
    }
  })
    .then(async (res) => {
      if (!res.ok) throw await res.json();
      return res.json();
    })
    .catch((err) => {
      error = err;
      console.log(err);
      return null;
    });

  if (error) {
    throw error;
  }

  return res;
};

export const saveNotepad = async (token: string = '', chat_id: string, content: string) => {
  let error = null;

  const res = await fetch(`${WEBUI_API_BASE_URL}/notepads/save`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      ...(token && { authorization: `Bearer ${token}` })
    },
    body: JSON.stringify({ chat_id: chat_id, content: content })
  })
    .then(async (res) => {
      if (!res.ok) throw await res.json();
      return res.json();
    })
    .catch((err) => {
      error = err;
      console.log(err);
      return null;
    });

  if (error) {
    throw error;
  }

  return res;
}; 