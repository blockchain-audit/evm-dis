




cfg:
	java -jar build/libs/Driver-java/evmdis.jar \
		--title $(NAME) \
		--cfg 100 $(BIN) \
		> out/$(NAME).dot
	dot -Tsvg out/$(NAME).dot -o out/$(NAME).svg

