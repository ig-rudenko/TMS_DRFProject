import {AxiosError} from "axios";

function getVerboseAxiosError(error: AxiosError<any>): string {
    console.log(error)
    if (error.response?.data) {
        const detail = error.response.data
        if (typeof detail === "string") return detail;
        if (typeof detail === "object") {
            let validationErrors = ""
            for (const detailElement in detail) {
                validationErrors += detailElement.toString().toUpperCase() + ": " + detail[detailElement].toString() + "\n"
            }
            return validationErrors
        }

    }
    return error.message
}


export default getVerboseAxiosError
