// intercepting all the request we send by adding all the correct headers. to make our life easier
import axios from 'axios';
import {ACCESS_TOKEN} from "./constants";
// import anything from the specified environment we chose
const api= axios.create({
    baseURL: import.meta.env.VITE_API_URL
})