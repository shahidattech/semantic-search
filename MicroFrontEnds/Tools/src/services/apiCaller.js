import axios from "axios";
import { getLocalStorage } from "./../utilities/setSession";

export async function handlePostCaller(payload, endpoint, gen_token = false, contentType = null) {
  // console.log('Endpoint:: ', endpoint)
  if (gen_token) {
    const headers = {
      'Content-Type': contentType || 'application/json',
      'API-KEY': config.API_KEY
    }
    return await axios.post(endpoint, payload, { headers: headers });
  }
  else {
    const accessToken = getLocalStorage("access_token") || '';
    const headers = { 'Authorization': 'Bearer ' + accessToken.replaceAll('"', '') };
    return await axios.post(endpoint, payload, { headers });
  }
}

export async function handlePutCaller(payload, endpoint) {
  // console.log('Endpoint:: ', endpoint)
  const headers = { 'Authorization': 'Bearer ' + getLocalStorage("access_token").replaceAll('"', '') };
  return await axios.put(endpoint, payload, { headers });
}

export async function handleDeleteCaller(endpoint) {
  // console.log('Endpoint:: ', endpoint)
  const headers = { 'Authorization': 'Bearer ' + getLocalStorage("access_token").replaceAll('"', '') };
  return await axios.delete(endpoint, { headers });
}

export async function handleGetCaller(endpoint) {
  //console.log('Endpoint:: ', endpoint)
  const headers = { 'Authorization': 'Bearer ' + getLocalStorage("access_token").replaceAll('"', '') };
  return await axios.get(endpoint, { headers });
}

export async function handleDownloadExcelCaller(endpoint) {
  // console.log('Endpoint:: ', endpoint)
  const headers = { 'Authorization': 'Bearer ' + getLocalStorage("access_token").replaceAll('"', ''), "Accept": "application/vnd.ms-excel" };
  return await axios({
    url: endpoint,
    method: "GET",
    headers: headers,
    responseType: "blob"
  });
}