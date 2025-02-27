# Variables
DOCKER_IMAGE=yyzhang4/open-webui
IMAGE_TAG=latest

# Build Docker images
build-dev:
	@echo "Building web Docker image: $(DOCKER_IMAGE):$(IMAGE_TAG)..."
	docker-compose -f docker-compose.build.yaml \
		--env-file .env.build \
		--build-arg BUILD_PLATFORM=linux/arm64 \
		--build-arg DOCKER_IMAGE=$(DOCKER_IMAGE) \
		--build-arg IMAGE_TAG=$(IMAGE_TAG) \
		build
	@echo "Web Docker image built successfully: $(DOCKER_IMAGE):$(IMAGE_TAG)"

build-prd:
	@echo "Building web Docker image: $(DOCKER_IMAGE):$(IMAGE_TAG)..."
	docker-compose -f docker-compose.build.yaml \
		--env-file .env.build \
		--build-arg BUILD_PLATFORM=linux/amd64 \
		--build-arg DOCKER_IMAGE=$(DOCKER_IMAGE) \
		--build-arg IMAGE_TAG=$(IMAGE_TAG) \
		build
	@echo "Web Docker image built successfully: $(DOCKER_IMAGE):$(IMAGE_TAG)"

# Push Docker images
push:
	@echo "Pushing web Docker image: $(DOCKER_IMAGE):$(IMAGE_TAG)..."
	docker push $(DOCKER_IMAGE):$(IMAGE_TAG)
	@echo "Web Docker image pushed successfully: $(DOCKER_IMAGE):$(IMAGE_TAG)"

release: build-prd push