install:
	@echo "Installing tfenv"
	@git clone https://github.com/tfutils/tfenv.git ~/.tfenv
	@echo 'export PATH="$$HOME/.tfenv/bin:$$PATH"' >> ~/.bashrc
	@echo 'eval "$$(tfenv init -)"' >> ~/.bashrc
	@source ~/.bashrc
	@tfenv install latest
	@tfenv use latest

deploy: install
	@echo "Deploying with Terraform"
	@terraform init -backend-config="access_key=${AWS_ACCESS_KEY}" -backend-config="secret_key=${AWS_SECRET_KEY}"
	@terraform plan -out=tfplan -var-file=terraform.tfvars
	@terraform apply -auto-approve -input=false tfplan

clean:
	@echo "Cleaning up Terraform deployment"
	@terraform destroy -auto-approve
