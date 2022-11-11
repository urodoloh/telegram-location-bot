import axios, { AxiosResponse } from 'axios';
import { EndedGamesResponse, User } from './types/getresponse.interface';


const instance = axios.create({
	baseURL: 'http://localhost:5000/api/',
	timeout: 15000,
});

const responseBody = (response: AxiosResponse) => response.data;

const requests = {
	get: (url: string) => instance.get(url).then(responseBody),
	post: (url: string, body: {}) => instance.post(url, body).then(responseBody),
	put: (url: string, body: {}) => instance.put(url, body).then(responseBody),
	delete: (url: string) => instance.delete(url).then(responseBody),
};

export const GetAPI = {
    getUsers: (): Promise<{userlist: User[]}> => requests.get('users'),
	getEndedGames: (): Promise<EndedGamesResponse> => requests.get('thegame')
}