import { WEBUI_API_BASE_URL } from '$lib/constants';

export const getEditorContent = async (token: string = '', chatId: string) => {
  let error = null;

  const searchParams = new URLSearchParams();
  searchParams.append('chatId', chatId);

  const res = await fetch(`${WEBUI_API_BASE_URL}/editor/content?${searchParams.toString()}`, {
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

export const saveEditorContent = async (token: string = '', chatId: string, content: string) => {
  let error = null;

  const res = await fetch(`${WEBUI_API_BASE_URL}/editor/content`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      ...(token && { authorization: `Bearer ${token}` })
    },
    body: JSON.stringify({ chatId: chatId, content: content })
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