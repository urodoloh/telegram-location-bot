import {useState, useEffect} from 'react';
import { GetAPI } from '../API';
import { UserlistI } from '../types/getresponse.interface';

export const useGetUserlist = () =>{
    const [list, setList] = useState<UserlistI>();
    const [isError, setIsError] = useState<boolean>(false);

    useEffect(() => {
        GetAPI.getUsers()
            .then((data) => {
                setList(data)
                console.log("useGetUserlist: true");
            })
            .catch((err) => {
                setIsError(true);
                console.log("useGetUserlist Error:", isError);
            });
    }, []);


    return list

}