import aiml

kernel = aiml.Kernel()
kernel.learn('botinho/std-startup.xml')
kernel.respond('load aiml b')

def get_reposta(mensagem):
	print(kernel.respond(mensagem).capitalize)
	return kernel.respond(mensagem)