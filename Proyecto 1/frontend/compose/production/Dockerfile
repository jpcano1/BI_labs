FROM node:12.21.0 AS build

ENV APP_DIR /app
WORKDIR $APP_DIR

ADD . $APP_DIR

RUN npm install

RUN npm run build --prod

FROM nginx:1.16.0-alpine
COPY --from=build /app/dist/frontend /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx","-g","daemon off;"]
