%define	rpm_macros_rev	1.271
Summary:	PLD Linux RPM build macros
Summary(pl):	Makra do budowania pakiet�w RPM dla Linuksa PLD
Name:		rpm-build-macros
Version:	%{rpm_macros_rev}
Release:	1
License:	GPL
Group:		Base
Source0:	rpm.macros
Source1:	service_generator.sh
Requires:	rpm-build
Provides:	rpmbuild(macros) = %{rpm_macros_rev}
Obsoletes:	rpm-macros
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rpmlibdir /usr/lib/rpm

%description
This package contains rpm build macros for PLD Linux.

%description -l pl
Ten pakiet zawiera makra rpm-a do budowania pakiet�w dla Linuksa PLD.

%prep
if ! awk '/^#.*Revision:.*Date/{exit($3 > %{rpm_macros_rev})}' %{SOURCE0}; then
	echo >&2 "Update rpm_macros_rev, it seems outdated"
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_rpmlibdir}
cp %{SOURCE0} $RPM_BUILD_ROOT%{_rpmlibdir}/macros.build
install %{SOURCE1} $RPM_BUILD_ROOT%{_rpmlibdir}/service_generator.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_rpmlibdir}/macros.build
%attr(755,root,root) %{_rpmlibdir}/service_generator.sh
