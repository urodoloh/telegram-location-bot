import axios, { AxiosResponse } from 'axios';
import { GameDataI, UserlistI, EndedGamesResponse } from './types/getresponse.interface';


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
    getUsers: (): Promise<UserlistI> => requests.get('users'),
    getEndedGamesForUser: (user_id: number): Promise<GameDataI>  => requests.get(`thegame/${user_id}`),
	getEndedGames: (): Promise<EndedGamesResponse> => requests.get('thegame')
}