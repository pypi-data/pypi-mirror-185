
## [yhmgit](http://gitlab.yonghui.cn/operation-xm-qdjg/yhgit): 一个多仓库管理插件

当项目存在多个组件依赖，我们可能有以下需求：

  需要在多个组件分别建立开发分支；同步多个组件的远程代码；提交多个组件的代码；合并开发分支到发布分支，并自动打tag
  
  以上需求分别基于每个组件进行操作，每项任务都将耗费大量的精力和时间。

  基于以上需求，开发了yhmgit插件，使用该插件可以很好的解决： 开发分支的创建，开发分支状态查看，开发分支代码拉取，开发分支代码提交，开发分支推送，开发分支合并，开发分支合并到发布分支并打tag


### 环境

- Python >= 3.0

### 安装

如果你已经下载了最新的源码:

    python3 setup.py install

或者你可以通过pypi安装

    pip3 install yhgit

这两个命令都将安装所需的包依赖项。

可以在以下位置获取分发包以进行手动安装

    http://pypi.python.org/pypi/yhgit

如果你想从源代码克隆，你可以这样做:


```bash
git http://gitlab.yonghui.cn/operation-xm-qdjg/yhgit
```

```
   table.add_row(
            [0, "install", "-b 指定分支名; 组件 指定 新建分支的组件", "根据分支branch，然后基于组件新建分支branch"])
        table.add_row([1, "install", "组件 指定 新建分支的组件",
                       "根据本地PodfileLocal.yaml中的配置，获取新分支branch，然后基于的组件新建分支branch"])
        table.add_row([2, "status", "", "根据本地PodfileLocal.yaml中配置的仓库，获取所有仓库的开发分支及仓库状态"])
        table.add_row([3, "commit", "-m 指定提交的信息", "根据本地PodfileLocal.yaml中配置的仓库，提交本地仓库中的修改"])
        table.add_row([4, "pull", "", "根据本地PodfileLocal.yaml中配置的仓库，拉取远端仓库中代码"])
        table.add_row([5, "push", "", "根据本地PodfileLocal.yaml中配置的仓库，推送本地代码到远端"])
        table.add_row([5, "merge", "-b 指定分支名; 组件 指定 merge的组件", "然后基于组件merge 分支到当前开发分支，并自动提交"])
        table.add_row([6, "release", "", "根据本地PodfileModule.yaml中配置的仓库，合并开发分支到master，并自动打新的tag"])
        table.add_row([7, "clean", "", "清空本地PodfileLocal.yaml 及 modules文件夹"])
```

### 说明文档

#### 1. 通过 yhgit install 拉取或者创建新分支

    -b 指定新建的分支名

```
    yhgit -b feature-test install SXFreshOrderModule    
```
#### 2. 通过 yhgit status 查看组件状态 


```
yhgit status
```

    根据本地PodfileLocal.yaml中配置的仓库，获取所有仓库的开发分支及仓库状态
  

#### 3. 通过 yhgit commit 提交本地修改

    -m 提交信息

```
yhgit commit -m '提交'
```


    执行pull_modules内部过程： 
    1. 如果path中不存在modules，先在path中新建modules目录，用于存放组件代码
    2. 根据PodfileLocal.yaml中组件的依赖，

          先判断是否存在目录， 如果本地没有组件对应目录，退出；

          存在目录：在当前新分支，直接拉取代码；

          存在目录：本地不在新分支，异常提示拉取失败，需要手动切换到开发分支

    3. 更新PodfileModule.yaml中依赖为分支，更新PodfileLocal .yaml中依赖为路径依赖
    
   
#### 4. 通过 push_modules 拉取开发分支最新代码

    exception_module_list： 这里面的组件不拉取最新代码

```
def push_modules(self, exception_module_list=[]):
```


    执行push_modules内部过程： 
    1. 如果path中不存在modules，先在path中新建modules目录，用于存放组件代码
    2. 根据PodfileModule.yaml中组件的依赖，

       先判断是否存在目录， 如果本地没有组件对应目录，提示异常；

       存在目录：在当前新分支，直接提交代码；

       存在目录：本地不在新分支，提示异常，需要手动切换到开发分支

 #### 5. 通过 merge_modules 拉取开发分支最新代码

    exception_module_list： 这里面的组件不拉取最新代码

````
def merge_modules(self, exception_module_list=[]):
````


    执行merge_modules内部过程： 
    1. 如果path中不存在tagpath，先在path中新建tagpath目录，用于临时存放组件代码
    2. 根据PodfileModule.yaml中组件的依赖： 

       clone开发分支代码；

       如果开发分支版本号大于master分支，那么新的版本号就是开发分支版本号，否则就自增1；

       更新版本号并提交代码；然后根据新版本号打tag，并提交到远端分支；

       更新PodfileModule.yaml中的依赖为tag，并清空PodfileLocal .yaml中的文件

    
### 怎么用

```
  # 新建一个python 文件
  # 引入依赖
  import yhmgit
  # 方法调用
  if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    cuPath = os.getcwd()
    fa_path = "../../Desktop/Project/yh-rme-srm-purchase-ios/"
    project_git = "http://gitlab.yonghui.cn/operation-pc-mid-p/yh-rme-srm-purchase-ios.git"
    # 分支的名字，如果没有指定将用年月日表示
    n_branch = "221107"

    yhgit = yhmgit.yhmgit(git=project_git, path=fa_path, n_branch=n_branch)
    # 初始化项目
    # yhgit.init_project(clean_proj=False)
    # 拉取远端代码
    # yhgit.pull_modules()
    # 提交本地代码
    # yhgit.push_modules()
    # 开发完成，合并开发分支打tag
    yhgit.merge_modules()
   

```

### 具体场景具体分析

1. 我要开始一个迭代，需要基于仓库"git@gitlab.yonghui.cn:operation-cp-hcwms/yhwms_flutter.git"，分支"master" 切一个开发分支a_branch，项目里的每个组件的新分支名为"dev/1.0.0", 工程放在"../../Desktop/Project/YHDOS/"
那么我可以通过
```
    fa_path = "../../Desktop/Project/YHDOS/"
    project_git = "git@gitlab.yonghui.cn:operation-cp-hcwms/yhwms_flutter.git"
    # 分支的名字，如果没有指定将用年月日表示
    c_branch = "master"
    n_branch = "dev/1.0.0"
    cb = yhmgit.yhmgit(git=project_git, branch=c_branch, tag="", path=fa_path, n_branch=n_branch)
    cb.init_project() 
    
    如果fa_path地址中本来就有代码，不想清空，但是还是要建开发分支，就可以通过cb.init_project(clean_proj=False) 来进行操作
```

1. 别人建好了一个开发分支，我需要基于这个分支进行开发。 

    1. 本地有项目仓库，先切到分支a_branch; 
        将fa_path 要改为本地项目地址；
        执行pull_modules，就会在项目目录下新建modules目录，并将所有组件的仓库放在这个目录中
        自动修改PodfileLocal.yaml中的依赖

```
    fa_path = "../../Desktop/Project/YHDOS/" # 改为本地仓库地址
    project_git = "git@gitlab.yonghui.cn:operation-cp-hcwms/yhwms_flutter.git"
    # 分支的名字，如果没有指定将用年月日表示
    c_branch = "master"
    n_branch = "dev/1.0.0"
    cb = yhmgit.yhmgit(git=project_git, branch=c_branch, tag="", path=fa_path, n_branch=n_branch)
    cb.pull_modules() 
```
        

