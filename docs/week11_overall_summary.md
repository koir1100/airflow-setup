## 개발환경 구축을 위한 Docker와 K8s 실습   
  
### 개념 요약  
  
1. Docker 란?  
  - 소프트웨어를 일관되게 빌드하고 실행하고 배포하는 환경
2. Docker 용어 정리  
  - Docker Image: 개발된 환경을 그대로 패키징하여 독립적으로 완전하게 만들어진 패키지  
  - Dockerfile: Docker Image를 구성하는 실행환경, 소프트웨어 자체, 필요 라이브러리, 파일 시스템 스냅샷, 환경 설정 변수, 메타 데이터 및 설치 관련 실행 순서 등이 기술된 파일  
  - Docker Container: 소프트웨어를 실행하기 위한 독립적이고 분리된 공간으로 Docker Engine 기반 동작하며, 자체 파일 시스템을 갖고 있음  
  - Docker Hub (hub.docker.com): Docker Image의 보관소인 Docker Registry에서 Cloud registry 가운데 가장 유명한 서비스로, Docker Image에 대한 공유 및 검색이 가능함   
  - Docker Compose: 다수의 Container로 소프트웨어가 구성되는 경우, 관리할 수 있는 툴이며, docker-compose.yml 파일을 통해 환경 설정이 가능함  
3. Docker 사용시 주의할 점  
  - 설정 가능한 Docker Volume 타입 가운데, host volumes는 개발시, named volumes는 실제 배포시 사용할 때 사용해야 함  
  - 실제 Production 환경에서 사용할 경우, 실행 중인 컨테이너에서 작업하지 않고, CI/CD 프로세스를 통해 새 이미지를 빌드한 다음, 실제 환경에 컨테이너 배포하는 자동화 수행되도록 구성하기  
    - 구체적으로, Docker Image를 통해 버전 관리 수행 및 컨테이너 배포 진행하되, 문제 발생할 경우 문제가 없는 이미지로 롤백할 수 있어야 함  
4. Kubernetes (K8s) 이란?  
  - Container 기반 서비스 배포, 스케일링 및 관리를 자동화해주는 오픈소스 프레임워크로, 물리 서버와 가상 서버 위에서 모두 동작함  
  - 모든 글로벌 클라우드 업체 지원: EKS(ECS) - AWS, AKS - MS Azure, GKS - Google Cloud  
  - 다수의 Container를 효율적으로 관리하기 위한 도구로, 이미지 배포, 스케일링(탄력적 운영), 네트워크(부하 분산), 인사이트(로깅, 서비스 문제 파악 및 분석) 등 다양한 기능 제공  
