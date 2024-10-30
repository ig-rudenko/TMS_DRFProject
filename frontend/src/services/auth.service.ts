import api from "./api";
import {tokenService} from "./token.service";
import {LoginUser, RegisterUser, UserTokens} from "./user";
import UserService from "./user.service";


interface TokenPair {
    access: string;
    refresh: string
}

const obtainTokenURL = "/jwt/"
const registerUserURL = "/v1/users/"


class AuthService {
    async login(user: LoginUser) {
        let response = await api.post<TokenPair>(obtainTokenURL, {
            username: user.username,
            password: user.password
        });

        if (response.data.access) {
            tokenService.setUser(new UserTokens(response.data.access, response.data.refresh || null));
        }
        return response
    }

    logout() {
        tokenService.removeUser();
        UserService.removeUser();
    }

    register(user: RegisterUser) {
        return api.post(registerUserURL, user);
    }
}

export default new AuthService();