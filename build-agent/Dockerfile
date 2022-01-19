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
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    openjdk-11-jre \
    nodejs \
    npm \
    apt-transport-https \ 
    gnupg \ 
    lsb-release \
  && rm -rf /var/lib/apt/lists/*

RUN curl -o - https://aquasecurity.github.io/trivy-repo/deb/public.key | apt-key add - && \
    echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | tee -a /etc/apt/sources.list.d/trivy.list && \
    apt-get update && apt-get install trivy


ARG AGENT_VERSION=2.194.0

WORKDIR /azp

ARG AZP_AGENTPACKAGE_URL=https://vstsagentpackage.azureedge.net/agent/${AGENT_VERSION}/vsts-agent-linux-x64-${AGENT_VERSION}.tar.gz
RUN curl -LsS "$AZP_AGENTPACKAGE_URL" | tar -xz

COPY ./start.sh .
RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]