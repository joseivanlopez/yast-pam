#
# spec file for package yast2-pam
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-pam
Version:        3.1.1
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0
url:            http://github.com/yast/yast-pam
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  rubygem(yast-rake)
# owners of some directories
BuildRequires:  yast2
Requires:	yast2

Requires:	pam-config >= 0.8

Provides:	yast2-agent-pam
Obsoletes:	yast2-agent-pam
Provides:	yast2-agent-pam-devel
Obsoletes:	yast2-agent-pam-devel

BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:	YaST2 - PAM Agent

%description
This agent is used by YaST2 to modify the PAM configuration files

%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%build

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%{yast_moduledir}/*
%{yast_scrconfdir}/*.scr
%{yast_agentdir}/ag_passwd
%doc %{yast_docdir}
