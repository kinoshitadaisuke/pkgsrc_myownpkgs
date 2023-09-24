# $NetBSD$

DISTNAME=	flake8-bugbear-23.9.16
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=f/flake8-bugbear/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/flake8-bugbear/
COMMENT=	Plugin for flake8 finding likely bugs
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-setuptools>=61.2:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-flake8>=6.0.0:../../devel/py-flake8
DEPENDS+=	${PYPKGPREFIX}-attrs>=19.2.0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-tox>=0:../../devel/py-tox
DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-hypothesis>=0:../../devel/py-hypothesis
DEPENDS+=	${PYPKGPREFIX}-hypothesmith>=0:../../devel/py-hypothesmith
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
