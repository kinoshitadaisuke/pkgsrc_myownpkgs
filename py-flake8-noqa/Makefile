# $NetBSD$

DISTNAME=	flake8-noqa-1.4.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=f/flake8-noqa/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/flake8-noqa/
COMMENT=	Flake8 noqa comment validation
LICENSE=	gnu-lgpl-v3

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm

DEPENDS+=	${PYPKGPREFIX}-flake8>=3.8.0:../../devel/py-flake8
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.0.0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=3.7.4.2:../../devel/py-typing-extensions

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
