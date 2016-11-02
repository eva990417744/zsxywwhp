from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from operator import attrgetter


def ez(id):
    hp = get_object_or_404(HP, pk=id)
    try:
        bufff = get_object_or_404(Buff, pk=1)
    except:
        bufff = get_object_or_404(Buff,pk=2)
    try:
        debufff = get_object_or_404(DeBuff, pk=1)
    except:
        debufff = get_object_or_404(DeBuff, pk=2)
    try:
        debuff_list = get_list_or_404(DeBuff, name=hp.name)
    except:
        debuff_list = ['none']
    try:
        buff_list = get_list_or_404(Buff, name=hp.name)
    except:
        buff_list = ['none']
    context = {
        'hp': hp,
        'debuff_list': debuff_list,
        'buff_list': buff_list,
        'bufff': bufff,
        'debufff': debufff
    }
    return context


def index(request):
    hp_list = get_list_or_404(HP)
    hp_list.sort(key=attrgetter('blood'), reverse=True)
    return render(request, 'hp/index.html', {'hp_list': hp_list})


def detailed(request, id):
    context = ez(id)
    return render(request, 'hp/detailed.html', context)


def buffchange(request, id, flag):
    hp = get_object_or_404(HP, pk=id)
    try:
        reason = request.POST
        if flag == 'buff':
            newbuff = Buff(name=hp.name, Buff_Reason=reason['reason'], Buff_Text=reason['text'],
                           key_id=hp.id)
        else:
            newbuff = DeBuff(name=hp.name, DeBuff_Reason=reason['reason'], DeBuff_Text=reason['text'],
                             key_id=hp.id)
    except:
        context = {'error': 'error no change'}
        return render(request, 'hp/error.html', context)
    else:
        newbuff.save()
        return HttpResponseRedirect('/hp/'+id+'/')
