import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

import networkx as nx
from graphviz import Digraph
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

transition_phrase=['comprises','includes','comprising','including','having','consisting']

Entity=['NN','NNS','NNP','NNPS']
Manner=['RB','RBR','RBS']
Value=['CD']
Attribute=['AD','JJ','JJR','JJS']

Verb=['VV','VB','VBD','VBP','VBZ','VBG','VBN']
Contain=transition_phrase
Prep=['P','IN','TO','RP','CC']

Concept=['Method','Step','Manner','Attribute','Entity','Value','Action','PrepHead','MannerHead']
Relation=['Verb','Contain','Prep','HasAtt']


def get_depparse(text):
	output = nlp.annotate(text, properties={
	  'annotators': 'tokenize,ssplit,pos,depparse',
	  'pipelineLanguage':'en',
	  'outputFormat': 'json'
	  })
	for sent in output['sentences']:
			sentence={}
			sentence['index']=sent['index']
			sentence['enhancedPlusPlusDependencies']=sent['enhancedPlusPlusDependencies']
			sentence['basicDependencies']=sent['basicDependencies']
			sentence['tokens']=[]
			for w in sent['tokens']:
				word={}
				word['index']=w['index']
				word['pos']=w['pos']
				word['word']=w['word']
				word['ontology']=define_ontology(word['word'], word['pos'])
				sentence['tokens'].append(word)

	#sentence=get_phrase(sentence)   #合并名词短语、固定短语等
	
	return sentence

def define_ontology(word,pos):
	if pos=='NN' and word.lower()=='method':
		ontology='Method'
	elif pos=='NN' and word.lower()=='step':
		ontology='Step'
	elif pos in Entity:
		ontology='Entity'
	elif pos in Manner:
		ontology='Manner'
	elif pos in Value:
		ontology='Value'
	elif pos in Prep:
		ontology='Prep'
	elif word.lower() in Contain:
		ontology='Contain'
	elif pos=='VBG' or pos=='VBN':  #may be an attribute or a verb
		ontology='Verb'
	elif pos in Attribute:
		ontology='Attribute'
	elif pos in Verb:
		ontology='Verb'
	else:
		ontology='～'
	return ontology

def get_phrase(sentence):
	phrase=[]
	remove_dep=[]
	for dep in sentence['enhancedPlusPlusDependencies']:
		if dep['dep'] in ['compound','mwe','compound:nn']:
			remove_dep.append(dep)
			if dep['dep'] in ['compound','compound:nn']:
				if dep['governor'] not in phrase:
					ph_index=list(range(dep['dependent'],dep['governor']+1))
					tmp_noun=''
					for i in ph_index:
						tmp_noun+=sentence['tokens'][i-1]['word']+'_'
					sentence['tokens'][dep['governor']-1]['word']=tmp_noun[:-1]
					phrase.append(dep['governor'])
					# print(sentence['tokens'][dep['governor']-1]['word'])
			elif dep['dep']=='mwe':
				sentence['tokens'][dep['governor']-1]['word']=dep['governorGloss']+'_'+dep['dependentGloss']
				# print(dep['governorGloss']+'_'+dep['dependentGloss'])
				phrase.append(dep['governor'])
			else:
				pass
	for dep in remove_dep:
		sentence['enhancedPlusPlusDependencies'].remove(dep)
	parse_list=[]
	for dep in sentence['enhancedPlusPlusDependencies']: #dep中的词替换短语等
		dep['governorGloss']=sentence['tokens'][dep['governor']-1]['word']
		dep['dependentGloss']=sentence['tokens'][dep['dependent']-1]['word']
		parse_list.append(dep)
	sentence['enhancedPlusPlusDependencies']=parse_list
	return sentence

def dep_edges(dep,g_label,d_label,sentence):
	edges=[]
	if dep['dep'] in ['nsubj','nsubjpass','nsubj:xsubj']:
		if d_label not in ['Method','Step','Entity']:  #修正词性解析错误导致的领域本体错误
			d_label='Entity'
		if dep['dep']=='case':
			d_label='Prep'
		edge=(d_label+'_'+dep['dependentGloss'],g_label+'_'+dep['governorGloss'])
		edges.append(edge)

	elif dep['dep']=='case':
		d_label='Prep'
		edge=(d_label+'_'+dep['dependentGloss'],g_label+'_'+dep['governorGloss'])
		edges.append(edge)

	elif dep['dep'] in ['mark']:
		edge1=(d_label+'_'+dep['dependentGloss'],'Action_'+dep['governorGloss'])
		edge2=('Action_'+dep['governorGloss'],g_label+'_'+dep['governorGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep'] in ['acl','acl:relcl','dobj','cc']:
		edge=(g_label+'_'+dep['governorGloss'],d_label+'_'+dep['dependentGloss'])
		edges.append(edge)

	elif dep['dep']=='acl:for':
		edge1=(g_label+'_'+dep['governorGloss'],'Prep_for')
		edge2=('Prep_for','Action_'+dep['dependentGloss'])
		edge3=('Action_'+dep['dependentGloss'],d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)
		edges.append(edge3)

	elif dep['dep'] in ['xcomp','ccomp']:
		edge1=(g_label+'_'+dep['governorGloss'],'Action_'+dep['dependentGloss'])
		edge2=('Action_'+dep['dependentGloss'],d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep'] in ['conj:and','nmod:of','nmod:based_on']:
		prep=dep['dep'].split(':')[-1]
		edge1=(g_label+'_'+dep['governorGloss'],'Prep_'+prep)
		edge2=('Prep_'+prep,d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep'] in ['conj']:
		print(dep)
		prep='and'
		for d in sentence['enhancedPlusPlusDependencies']:
			if d['dep']=='cc' and d['governorGloss']==dep['governorGloss']:
				prep=d['dependentGloss']
		edge1=(g_label+'_'+dep['governorGloss'],'Prep_'+prep)
		edge2=('Prep_'+prep,d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep'] in ['nmod:in','nmod:according_to','nmod:with','nmod:to','nmod:from']:
		prep=dep['dep'].split(':')[-1]
		edge1=(g_label+'_'+dep['governorGloss'],'PrepHead_'+prep)
		edge2=('PrepHead_'+prep,'Prep_'+prep)
		edge3=('Prep_'+prep,d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)
		edges.append(edge3)

	elif dep['dep'] in ['nmod:npmod']:
		edge1=(d_label+'_'+dep['dependentGloss'],'HasAtt_'+dep['governorGloss'])
		edge2=('HasAtt_'+dep['governorGloss'],g_label+'_'+dep['governorGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep'] in ['amod','nummod']:
		if dep['dep']=='amod':   #修正词性解析错误导致的领域本体错误
			g_label='Entity'
			d_label='Attribute'
		edge1=(g_label+'_'+dep['governorGloss'],'HasAtt_'+dep['dependentGloss'])
		edge2=('HasAtt_'+dep['dependentGloss'],d_label+'_'+dep['dependentGloss'])
		edges.append(edge1)
		edges.append(edge2)

	elif dep['dep']=='advmod':
		if g_label in ['Verb','Contain']:
			edge1=(g_label+'_'+dep['governorGloss'],'MannerHead_'+dep['dependentGloss'])
			edge2=('MannerHead_'+dep['dependentGloss'],'HasAtt_'+dep['dependentGloss'])
			edge3=('HasAtt_'+dep['dependentGloss'],'Manner'+'_'+dep['dependentGloss'])
			edges.append(edge1)
			edges.append(edge2)
			edges.append(edge3)

		else:
			edge1=(g_label+'_'+dep['governorGloss'],'HasAtt_'+dep['dependentGloss'])
			edge2=('HasAtt_'+dep['dependentGloss'],d_label+'_'+dep['dependentGloss'])
			edges.append(edge1)
			edges.append(edge2)
	else:
		pass

	return edges

def get_nodes_edges(sentence):
	g=nx.DiGraph()
	for dep in sentence['enhancedPlusPlusDependencies']:
		g_pos=sentence['tokens'][dep['governor']-1]['pos']
		g_label=sentence['tokens'][dep['governor']-1]['ontology']
		d_pos=sentence['tokens'][dep['dependent']-1]['pos']
		d_label=sentence['tokens'][dep['dependent']-1]['ontology']
		edges=dep_edges(dep, g_label, d_label,sentence)
		g.add_edges_from(edges)
	return g.nodes(),g.edges()

def create_graph(nodes,edges,number=0):
	dot=Digraph(comment=number,format='png')
	for n in nodes:
		if n.split('_')[0] in Concept:
			shape='rectangle'
		else:
			shape='ellipse'
		dot.node(n,n,shape=shape)
	for e in edges:
		dot.edge(e[0],e[1])
	#dot.save(str(number)+'.gv','/home/ttt/graph/')
	dot.render('D:\HuaWei\hello\hello\graph'+str(number)+'.gv', view=False)



if __name__=='__main__':
	sentences=['A mobile terminal for communicating with a refrigerator, the mobile terminal comprises tmp_word.',
	           'The terminal comprises a communication unit configured to receive an electronic receipt containing purchased article information from a settlement terminal.',
	           'The terminal comprises a communication unit configured to receive storage article information from the refrigerator.',
	           'The purchased article information identify at least one purchased article that has been purchased.',
	           'The storage article information identifying at least one stored article that is stored in the refrigerator.',
	           'A display unit configured to display the purchased article information and the storage article information.',
	           'A controller configured to update the storage article information using the purchased article information based on a user input.'
	           ]

	# sentences=['The terminal comprises a communication unit configured to receive an electronic receipt containing purchased article information from a settlement terminal.']
	i =0
	for text in sentences:
		sentence=get_depparse(text)
		sentence=get_phrase(sentence)   #合并短语
		# for dep in sentence['enhancedPlusPlusDependencies']:
		# 	print(dep)
		nodes,edges=get_nodes_edges(sentence)
		create_graph(nodes, edges,number=i)
		i+=1
		

