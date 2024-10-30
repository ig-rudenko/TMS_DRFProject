import {createApp} from 'vue';
import PrimeVue from 'primevue/config';
import Ripple from 'primevue/ripple';
import ToastService from 'primevue/toastservice';
import Tooltip from 'primevue/tooltip';
import Avatar from "primevue/avatar";
import Button from "primevue/button";
import ColorPicker from "primevue/colorpicker";
import Dialog from "primevue/dialog";
import DatePicker from "primevue/datepicker";
import InputText from "primevue/inputtext";
import Message from "primevue/message";
import Menubar from "primevue/menubar";
import MultiSelect from "primevue/multiselect";
import Badge from "primevue/badge";
import FloatLabel from "primevue/floatlabel";
import FileUpload from "primevue/fileupload";
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import Textarea from "primevue/textarea";
import Paginator from "primevue/paginator";
import "primeicons/primeicons.css";
import "@/style.css";
import "@/assets/base.css"
import { CkeditorPlugin } from '@ckeditor/ckeditor5-vue';

import App from "@/App.vue";

import router from "@/router";
import store from "@/store";
import setupInterceptors from "@/services/setupInterceptors.ts";

setupInterceptors();
export const app = createApp(App);
app.use(PrimeVue, {ripple: true, theme: 'none'});
app.use(ToastService);
app.use(store);
app.use(router);
app.use(CkeditorPlugin);

app.directive('ripple', Ripple);
app.directive('tooltip', Tooltip);

app.component("Avatar", Avatar)
app.component('Badge', Badge);
app.component("Button", Button);
app.component("ColorPicker", ColorPicker);
app.component("DatePicker", DatePicker);
app.component("Dialog", Dialog);
app.component("InputText", InputText);
app.component("FileUpload", FileUpload);
app.component("Menubar", Menubar);
app.component("Message", Message);
app.component("MultiSelect", MultiSelect);
app.component('FloatLabel', FloatLabel);
app.component('Paginator', Paginator);
app.component("Splitter", Splitter);
app.component("SplitterPanel", SplitterPanel);
app.component("Textarea", Textarea);

app.mount("#app");
