FROM jekyll/builder:3.0.2
WORKDIR /src
RUN apk add --update --no-cache build-base
COPY Gemfile /src
COPY Gemfile.lock /src
RUN bundle install
