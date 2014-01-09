################################################################
####menu.py#####################################################
################################################################

################################
####title#######################
################################  
if request.function == 'index':
    response.title = 'hospitalityfor'
else:
    response.title = request.function

################################
####meta########################
################################ 
response.meta.author = 'Trevor Overman'
response.meta.description = 'the internet is hospitable'
response.meta.keywords = 'internet, hospitality, loving, evolution, transparent'
response.meta.generator = 'the guest is god'
