from IPython.display import FileLink, FileLinks
import os

def set_ppm_path(path):
    '''
        This function sets the path to the NuGrid VOSpace directory as a
        global variable, so that it need only be set once during an inter-
        active session.
        '''
    global ppm_path
    ppm_path=path

def list_runs(run=''):
    '''
    Retrieve a list of all available PPM Yprofile sequences.
        
    Parameters
    ----------
    run : string
        If passed, list_runs returns all runs within the given top-level run.
        If not given (empty string), list the top-level runs.
    '''

    try:
        list=os.listdir(ppm_path+'/'+run)
    except:
        print 'This run does not seem to exist.'
    runs=[l for l in list if os.path.isdir(os.path.join(ppm_path+'/'+run, l))]
    for r in runs:
        print r


def grab_session(name,format='ipynb'):
    '''
    Get a download link a notebook session in either .ipynb or static
    rendered html format.
    If .ipynb format, the file will have the additional extension
    .ppm, which one must remove before using again.
        
    Parameters
    ----------
    name : string
        The name of the session that you want to grab.
        
    Examples
    --------
    
    grab_session('my_first_notebook')
    '''
    if '.ipynb' not in name: name += '.ipynb'
    if format == 'ipynb':
        # append .ppm extension to avoid interpretation issues:
        name2 = name+'.ppm'
        os.system('cp '+name+' '+name2)
    else:
        # render the notebook into static html using nbconvert
        print 'rendering html notebook...'
        os.system('ipython nbconvert '+name)
        name2 = name.replace('.ipynb','.html')
    
    try:
        return FileLink(name2)
    except:
        print 'session '+name+' not available.'

def load_session(name,vos=False):
    '''
    Load a notebook session from either VOspace (only for
    authenticated users) or from a public GitHub repository.
        
    The notebook will appear in the notebook home directory.
        
    Parameters
    ----------
    name : string
        The name of the notebook session to load. This is either
        the full URL of the .ipynb file in the GitHub repository
        or the name of the notebook as it appears in your VOSpace
        notebook directory.
    vos : boolean, optional
        Is the notebook session to be loaded from your VOSpace?
        (For authenticated users only)
        The default is False.
    '''

    if not vos:
        try:
            os.system("wget "+name)
        except:
            print 'could not get '+name
    else:
        print "vcp from user's VOSpace is not yet implemented"

    if ".ppm" in name:
        os.rename(name.split('/')[-1],name.split('/')[-1].replace('.ppm',''))


def save_session(name):
    '''
    Permanently save a notebook session in the user's VOSpace.
    (only for authenticated users)
    '''

    print "vcp to user's VOSpace is not yet implemented"













