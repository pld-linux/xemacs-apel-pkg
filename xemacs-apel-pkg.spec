Summary:	A Portable Emacs Library - used by XEmacs MIME support
Summary(pl):	Przeno¶na biblioteka Emacsa - u¿ywana przez obs³ugê MIME XEmacsa
Name:		xemacs-apel-pkg
%define 	srcname	apel
Version:	1.25
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	532f6290f85b87e78eeb059eb8a3f673
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
Przeno¶na biblioteka Emacsa. U¿ywana przez obs³ugê MIME dla XEmacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/apel/README.ja lisp/apel/README.en lisp/apel/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
