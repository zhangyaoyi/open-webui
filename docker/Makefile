# Variables
DOCKER_REPOSITORY=yyzhang4/open-webui
IMAGE_TAG=latest

# Build Docker images
build-dev:
	@echo "Building web Docker image: $(DOCKER_REPOSITORY):$(IMAGE_TAG)..."
	docker-compose -f docker-compose.build.yaml \
		--env-file .env.build \
		build \
		--build-arg BUILD_PLATFORM=linux/arm64 \
		--build-arg DOCKER_REPOSITORY=$(DOCKER_REPOSITORY) \
		--build-arg IMAGE_TAG=$(IMAGE_TAG)
		
	@echo "Web Docker image built successfully: $(DOCKER_REPOSITORY):$(IMAGE_TAG)"

build-prd:
	@echo "Building web Docker image: $(DOCKER_REPOSITORY):$(IMAGE_TAG)..."
	docker-compose -f docker-compose.build.yaml \
		--env-file .env.build \
		build \
		--build-arg BUILD_PLATFORM=linux/amd64 \
		--build-arg DOCKER_REPOSITORY=$(DOCKER_REPOSITORY) \
		--build-arg IMAGE_TAG=$(IMAGE_TAG)

	@echo "Web Docker image built successfully: $(DOCKER_REPOSITORY):$(IMAGE_TAG)"

# Push Docker images
push:
	@echo "Pushing web Docker image: $(DOCKER_REPOSITORY):$(IMAGE_TAG)..."
	docker push $(DOCKER_REPOSITORY):$(IMAGE_TAG)
	@echo "Web Docker image pushed successfully: $(DOCKER_REPOSITORY):$(IMAGE_TAG)"

release: build-prd push