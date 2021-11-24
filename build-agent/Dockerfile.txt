FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN echo "APT::Get::Assume-Yes \"true\";" > /etc/apt/apt.conf.d/90assumeyes

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    jq \
    git \
    iputils-ping \
    libcurl4 \
    libicu-dev \
    libunwind8 \
    netcat \
    libssl1.0 \
    docker.io \
    python-dev \ 
  && rm -rf /var/lib/apt/lists/*



ARG AGENT_VERSION=2.194.0

WORKDIR /azp

ARG AZP_AGENTPACKAGE_URL=https://vstsagentpackage.azureedge.net/agent/${AGENT_VERSION}/vsts-agent-linux-x64-${AGENT_VERSION}.tar.gz
RUN curl -LsS "$AZP_AGENTPACKAGE_URL" | tar -xzv

COPY ./start.sh .
RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]