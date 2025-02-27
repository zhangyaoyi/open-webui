# Variables
DOCKER_REGISTRY=yyzhang4
DOCKER_IMAGE=$(DOCKER_REGISTRY)/open-webui
VERSION=latest

# Build Docker images
build-dev:
	@echo "Building web Docker image: $(DOCKER_IMAGE):$(VERSION)..."
	docker-compose -f docker-compose.build.yaml --env-file .env.build build --build-arg BUILD_PLATFORM=linux/arm64
	@echo "Web Docker image built successfully: $(DOCKER_IMAGE):$(VERSION)"

build-prd:
	@echo "Building web Docker image: $(DOCKER_IMAGE):$(VERSION)..."
	docker-compose -f docker-compose.build.yaml --env-file .env.build build --build-arg BUILD_PLATFORM=linux/amd64
	@echo "Web Docker image built successfully: $(DOCKER_IMAGE):$(VERSION)"

# Push Docker images
push:
	@echo "Pushing web Docker image: $(DOCKER_IMAGE):$(VERSION)..."
	docker push $(DOCKER_IMAGE):$(VERSION)
	@echo "Web Docker image pushed successfully: $(DOCKER_IMAGE):$(VERSION)"

release: build-prd push