import axiosInstance from "./api";
import {tokenService} from "./token.service";
import {refreshAccessToken} from "./token.refresh";

const ignoreURLs = ["/jwt/", "/v1/users/"];

const setup = () => {
    axiosInstance.interceptors.request.use(
        (config) => {
            const token = tokenService.getLocalAccessToken();
            if (ignoreURLs.indexOf(config.url || "") < 0 && token) {
                config.headers["Authorization"] = 'Bearer ' + token;
            }
            console.log(config.url)
            return config;
        },
        (error) => {
            return Promise.reject(error);
        }
    );

    axiosInstance.interceptors.response.use(
        res => res,
        async (err) => {
            const originalConfig = err.config;

            if (ignoreURLs.indexOf(originalConfig.url) < 0 && err.response) {
                // Access Token was expired
                if (err.response.status === 403 && !originalConfig._retry) {
                    originalConfig._retry = true;
                    originalConfig.headers["Content-Type"] = "application/json";

                    try {
                        const status = await refreshAccessToken(tokenService)

                        if (status) return axiosInstance(originalConfig);

                        return Promise.reject(err)
                    } catch (_error) {
                        localStorage.removeItem("user")
                        return Promise.reject(_error);
                    }
                }
            }

            return Promise.reject(err);
        }
    );
};

export default setup;