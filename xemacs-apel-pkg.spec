Summary:	A Portable Emacs Library - used by XEmacs MIME support
Summary(pl):	Przeno�na biblioteka Emacsa - u�ywana przez obs�ug� MIME XEmacsa
Name:		xemacs-apel-pkg
%define 	srcname	apel
Version:	1.20
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Portable Emacs Library. Used by XEmacs MIME support.

%description -l pl
Przeno�na biblioteka Emacsa. U�ywana przez obs�ug� MIME dla XEmacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/apel/README.ja lisp/apel/README.en lisp/apel/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/apel/README.ja.gz lisp/apel/README.en.gz lisp/apel/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
