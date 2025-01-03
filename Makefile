#Env vars
include	.env
export


# UV environment setup target
uv:
	@echo "$(GREEN)Setting up UV environment...$(NC)"
	@bash setup.sh