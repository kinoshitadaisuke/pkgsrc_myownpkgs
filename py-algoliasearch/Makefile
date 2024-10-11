# $NetBSD$

DISTNAME=	algoliasearch-4.6.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/algoliasearch/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/algoliasearch/
COMMENT=	Python API client to interact with Algolia
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-tox>=0:../../devel/py-tox
DEPENDS+=	${PYPKGPREFIX}-mypy>=0:../../lang/py-mypy
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-types-requests>=0:../../pkgsrc_myownpkgs/py-types-requests

#.include "../../lang/python/egg.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
