# $NetBSD$

DISTNAME=	doit-0.36.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=d/doit/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://pydoit.org
COMMENT=	doit - Automation Tool
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-cloudpickle>=0:../../converters/py-cloudpickle
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.4:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-flakes>=0:../../devel/py-flakes
DEPENDS+=	${PYPKGPREFIX}-codestyle>=0:../../devel/py-codestyle
DEPENDS+=	${PYPKGPREFIX}-test>=7.1.0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-coverage>=6.0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-tomli>=0:../../textproc/py-tomli
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-sphinx-press-theme>=0:../../pkgsrc_myownpkgs/py-sphinx-press-theme
DEPENDS+=	${PYPKGPREFIX}-sphinx-sitemap>=0:../../pkgsrc_myownpkgs/py-sphinx-sitemap
DEPENDS+=	${PYPKGPREFIX}-sphinx-reredirects>=0:../../pkgsrc_myownpkgs/py-sphinx-reredirects

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
