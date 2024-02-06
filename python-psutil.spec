# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-psutil
Epoch: 100
Version: 5.9.6
Release: 1%{?dist}
Summary: Process and system utilities module for Python
License: BSD-3-Clause
URL: https://github.com/giampaolo/psutil/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
psutil is a module providing an interface for retrieving information on
all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python 3, implementing many
functionalities offered by command line tools such as: ps, top, df,
kill, free, lsof, free, netstat, ifconfig, nice, ionice, iostat, iotop,
uptime, pidof, tty, who, taskset, pmap.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-psutil
Summary: Process and system utilities module for Python
Requires: python3
Provides: python3-psutil = %{epoch}:%{version}-%{release}
Provides: python3dist(psutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-psutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(psutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-psutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(psutil) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-psutil
psutil is a module providing an interface for retrieving information on
all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python 3, implementing many
functionalities offered by command line tools such as: ps, top, df,
kill, free, lsof, free, netstat, ifconfig, nice, ionice, iostat, iotop,
uptime, pidof, tty, who, taskset, pmap.

%files -n python%{python3_version_nodots}-psutil
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-psutil
Summary: Process and system utilities module for Python
Requires: python3
Provides: python3-psutil = %{epoch}:%{version}-%{release}
Provides: python3dist(psutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-psutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(psutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-psutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(psutil) = %{epoch}:%{version}-%{release}

%description -n python3-psutil
psutil is a module providing an interface for retrieving information on
all running processes and system utilization (CPU, memory, disks,
network, users) in a portable way by using Python 3, implementing many
functionalities offered by command line tools such as: ps, top, df,
kill, free, lsof, free, netstat, ifconfig, nice, ionice, iostat, iotop,
uptime, pidof, tty, who, taskset, pmap.

%files -n python3-psutil
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
